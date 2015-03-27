# dsopz

DSOpz (Datastore Operationz) is a project where you manage your datastore from your local machine.

## Features

 * Python API and command line
 * Export, import and delete data
 * GQL query
 * CSV exporter
 * Entity processors
   * You can update entities
   * Manage indexed properties
 * OAuth2 integrated
   * Installed apps
   * Service account

## Gettings Started

 * Every command has `--help`. 
 * If `namespace` was not given, we will access your default one.
 * If `kinds` was not given, we will use all of them

Login

    python src/oauth_installed.py

Export data

    python src/exporter.py -d gae-project -n namespace -k kind1 kind2 > entities.bak

GQL exporter

    python src/reader.py -d gae-project -n namespace -q 'select * from kind1' > entities.bak

Import data

    cat entities.bak | pyhton src/importer.py -d gae-project -d namespace -o upsert

You can import entities to another project or namespace.

Delete data

  You need just a keys-only file to delete, and you can extract it using `-o true` while exporting

    cat entities.bak | pyhton src/importer.py -d gae-project -d namespace -o delete

As you can see, all commands use stdin or stdout to read/write entities. The file has one entity json per line. You will want to use ` | gzip` and `| gunzip` to manage large amount of entities.

## Processors

Processors is what you can do to manage your entities file before import (or delete) it back do datastore. Just like this sample command:

    cat entities.bak | python src/processor.py -k kind1 kind2 -c col1 col2 > processed.bak
    cat processed.bak | python src/importer.py -d gae-project -n namespace -o upsert 

You can process a entity file to generate another file

Processors are the way you manage entities, one by one (or block by block). It always is appli



