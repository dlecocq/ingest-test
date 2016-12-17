*Objective:* Transform a set of CSV-format data into the LiveStories data model format.

At https://catalog.data.gov/dataset/civil-rights-data-collection-2013-14 you will find a 
ZIP archive, `crdc201314csv.zip`, containing the CSV-format file
`CRDC2013_14_SCH.csv`. This data file reports a set of racial and scholastic
demographics of all primary and secondary public schools in the U.S. for the
year 2013. Each recorded metric represents the absolute student count
of a particular demographic. Your task is to transform these metrics into
the LiveStories data model form.

The first row of the input file represents respective names of the data fields.
For this project
the only fields of interest are `LEAID` (school district identifier) and anything
suffixed as `_M` or `_F` (e.g. `SCH_PSENR_HI_M`), representing the male or female
population count of a particular demographic. You'll find descriptions for
these fields in file `CRDC2013_14_SCH_content.csv`. All demographics are
discriminated by sex (i.e. male or female), these must be aggregated and
reported as a unisex metric (sex-specific demographics should also be reported).

Each row of the input file represents all metrics recorded for a single school
but metrics at this granularity can be quite
sparse (i.e. non-reported), for this reason all metrics
must be aggregated and reported at the _school district_ level. 
Any metric recorded as a negative value should be treated as `0`.

The LiveStories data model format is a simple tabular format for representing
spacetime-oriented metrics. A recorded metric is encoded as a
linefeed-delimited record composed of tab-delimited values. A metric record
consists of the following fields, order respective.

```
PLACE TIME METRIC VALUE
```

* PLACE - unique identifier representing metric's associated location (e.g. `0100002`)
* TIME - an absolute UTC-zone time qualifier of the form `YYYYMMDDHHmmSS`, where all fields are optional
but year.
* METRIC - metric identifier (e.g. `SCH_PSENR_HI_M`)
* VALUE - metric value (e.g. `34`)

As a concrete example, the following source data...

```
LEAID,SCHID,SCH_PSENR_M,SCH_PSENR_F,SCH_PSENR_HI_M,SCH_PSENR_HI_F
0100000,01705,100,92,12,16
0100000,01862,51,50,8,-9
0100001,01923,68,73,3,5
0100001,01962,12,10,0,1
```

...would produce the following result...


```
0100000 2013 SCH_PSENR_M 151
0100000 2013 SCH_PSENR_F 142
0100000 2013 SCH_PSENR 293
0100000 2013 SCH_PSENR_HI_M 20
0100000 2013 SCH_PSENR_HI_F 16
0100000 2013 SCH_PSENR_HI 36
0100001 2013 SCH_PSENR_M 80
0100001 2013 SCH_PSENR_F 83
0100001 2013 SCH_PSENR 163
0100001 2013 SCH_PSENR_HI_M 3
0100001 2013 SCH_PSENR_HI_F 6
0100001 2013 SCH_PSENR_HI 9
```

(Note: `SCH_PSENR` and `SCH_PSENR_HI` are unisex aggregate metrics)

*Development*

This comes with a `Vagrantfile` with everything needed to provision a development
environment:

```bash
# Create and provision
vagrant up

# Log into the vagrant box
vagrant ssh

# Move to the code, activate the virtualenv and make the tests
cd /vagrant
source venv/bin/activate
make test
```

*Tests*

Tests require 100% code coverage, and are run with `make test`.
