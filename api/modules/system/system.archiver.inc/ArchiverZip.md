# ArchiverZip

- **Type:** Class
- **File:** [`modules/system/system.archiver.inc`](_file.md), lines 78–139 · [local source](../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L78-L139)
- **Module/theme:** system

## Signature

```php
class ArchiverZip implements ArchiverInterface
```

## Documentation

```text
Archiver for .zip files.

@link http://php.net/zip
```

## Properties

### $zip

```php
protected $zip;
```

```text
The underlying ZipArchive instance that does the heavy lifting.

@var ZipArchive
```

## Methods (derived index)

- [__construct()](ArchiverZip/__construct.md)
- [add()](ArchiverZip/add.md)
- [remove()](ArchiverZip/remove.md)
- [extract()](ArchiverZip/extract.md)
- [listContents()](ArchiverZip/listContents.md)
- [getArchive()](ArchiverZip/getArchive.md) — Retrieve the zip engine itself.

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
