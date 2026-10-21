# ArchiverTar

- **Type:** Class
- **File:** [`modules/system/system.archiver.inc`](_file.md), lines 11–71 · [local source](../../../../source/modules/system/system.archiver.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc#L11-L71)
- **Module/theme:** system

## Signature

```php
class ArchiverTar implements ArchiverInterface
```

## Documentation

```text
Archiver for .tar files.
```

## Properties

### $tar

```php
protected $tar;
```

```text
The underlying Archive_Tar instance that does the heavy lifting.

@var Archive_Tar
```

## Methods (derived index)

- [__construct()](ArchiverTar/__construct.md)
- [add()](ArchiverTar/add.md)
- [remove()](ArchiverTar/remove.md)
- [extract()](ArchiverTar/extract.md)
- [listContents()](ArchiverTar/listContents.md)
- [getArchive()](ArchiverTar/getArchive.md) — Retrieve the tar engine itself.

---
_Drupal 7.103 · [modules/system/system.archiver.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.archiver.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
