"""
This module provides a generic file reader.
"""

__all__ = ["read_file"]

import numpy as np
import pandas as pd


def read_file(data_filename):
    """
    Read a file.

    Parameters
    ----------
    data_filename: str
        A file to read.

    Returns
    -------
    data: str

    Examples
    --------
    """

    packet_data = np.fromfile(data_filename, dtype=">u2")
    #  find the packet starts
    start_indices = np.where(packet_data == 0xFE6B)[0]
    num_packets = len(start_indices)
    max_hits = int(np.ceil((len(packet_data) - num_packets * 7) / 2))
    timestamps = np.zeros(max_hits, np.uint64)
    pixel_ids = np.zeros(max_hits, np.uint16)
    hit_energy = np.zeros(max_hits, np.uint16)
    hit_count = 0  #  a rolling counter of the number of hits
    for count, this_index in enumerate(start_indices[:-1]):
        this_packet = packet_data[this_index : start_indices[count + 1]]
        if valid_packet(this_packet, "photon"):
            packet_length = this_packet[2]
            time_stamp = (this_packet[3] >> 24 | this_packet[4] >> 16 | this_packet[5]).astype(np.uint64)
            num_hits = int((packet_length - 7) / 2)
            hit_data = this_packet[7 : 7 + 2 * num_hits]
            pixel_ids[hit_count : hit_count + num_hits] = hit_data[::2]
            hit_energy[hit_count : hit_count + num_hits] = hit_data[1::2]
            timestamps[hit_count : hit_count + num_hits] = np.repeat(
                time_stamp, num_hits
            ).astype(np.uint64)

            hit_count += num_hits

    # remove the empty values
    good_index = timestamps != 0
    photon_list = pd.DataFrame(
        data={
            "timestamp": timestamps[good_index],
            "pixel_id": pixel_ids[good_index],
            "energy": hit_energy[good_index],
        }
    )

    return photon_list


def valid_packet(data, packet_type):
    """
    Validate a packet by applying a variety of tests.

    Parameters
    ----------
    data: np.array
        The packet data.
    
    packet_type: str
        The type of packet

    Returns
    -------
    result: bool

    """

    if packet_type == "photon":
        packet_length = data[3]

        # check that the length of the packet field is within expectaions
        if (packet_length < 9) or (packet_length % 2 != 1):
            return False

        # check that the checksum is correct
        if np.bitwise_xor.reduce(data) != 0:
            return False
        return True
