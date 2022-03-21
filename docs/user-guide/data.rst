.. _data:

****
Data
****

Overview
========

Data Description
----------------
XDSOX has two primary data products which originate from the same measurements.

#. an x-ray spectrum, provided regularly and 
#. a x-ray photon list provided on-demand.

Generally, the photon list data product will only exist during large flares and calibration periods.
This photon list will be used to generate an x-ray spectrum that supersedes the histogram data product.

The data levels for the spectrum product are described below.

+----------+---------------------------------------+---------------------------------------+
| Level    | Product                               | Description                           |      
+==========+=======================================+=======================================+
| 1        | Count Spectrum in energy space with   | FITS file, produced at least every 1 s|
|          | decimated counts in the lower energy  | gain calibrated for each pixel        |
|          | bins                                  |                                       |
+----------+---------------------------------------+---------------------------------------+

The data levels for the photon list product are described below.

+----------+---------------------------------------+---------------------------------------+
| Level    | Product                               | Description                           |      
+==========+=======================================+=======================================+
| 0        | List of photons. Each photon has      | FITS file, produced at least every 1 s|
|          | relative time, photon energy in ADC   |                                       |
|          | counts.                               |                                       |
+----------+---------------------------------------+---------------------------------------+
| 1        | List of photons. Each photon has      | FITS file, produced with a fixed      |
|          | time of arrival in UTC and calibrated | number photons and variable           |                       
|          | energy                                | integration times.                    |
+----------+---------------------------------------+---------------------------------------+

Both of the above products can be used to generate a calibrated spectrum product.

+----------+---------------------------------------+---------------------------------------+
| Level    | Product                               | Description                           |      
+==========+=======================================+=======================================+
| 2        | Flux Spectrum in energy space         | FITS, data flag to state if it was    |
|          |                                       | generated from the photon list        |
+----------+---------------------------------------+---------------------------------------+

The above data product will be used to generate the following derived data products.

+----------+---------------------------------------+---------------------------------------+
| Level    | Product                               | Description                           |      
+==========+=======================================+=======================================+
| 3        | Flare X-ray Directivity as a function | FITS file, requires Solar Orbiter STIX|
|          | of energy and time.                   | data                                  |
+----------+---------------------------------------+---------------------------------------+
| 4        | Flare-accelerated Electron Anisotropy | FITS file, requires modeling analysis |
|          | as a function of energy and time.     |                                       |
+----------+---------------------------------------+---------------------------------------+

File Naming Conventions
-----------------------

The file naming conventions for the products listed above are

#. padre_xdsox_l0_photonlist_%Y%m%d_%H%M%S_v{version}
#. padre_xdsox_l1_spec_%Y%m%d_%H%M%S_v{version}
#. padre_xdsox_l2_spec_%Y%m%d_%H%M%S_v{version}
#. padre_xdsox_l3_xraydirect_%Y%m%d_%H%M%S_v{version}
#. padre_xdsox_l4_eanisotropy_%Y%m%d_%H%M%S_v{version}

Specified using Python datetime strftime definitions and version is a 3 digit zero-padded number which begins at 000 and increments every time the file is reprocessed.
See `Python strftime cheatsheet <https://strftime.org/>`_ for a quick reference.

Getting Data
============

To be written.

Reading Data
============



Calibrating Data
================
Data products below level 2 generally require calibration to be transformed into scientificically useable units.
This section describes how to calibrate data files from lower to higher levels.