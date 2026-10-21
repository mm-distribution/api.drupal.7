# TestFileTransfer

- **Type:** Class
- **File:** [`modules/simpletest/tests/filetransfer.test`](_file.md), lines 95–150 · [local source](../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L95-L150)
- **Module/theme:** batch_test

## Signature

```php
class TestFileTransfer extends FileTransfer
```

## Documentation

```text
Mock FileTransfer object for test case.
```

## Properties

### $host

```php
protected $host = NULL;
```

### $username

```php
protected $username = NULL;
```

### $password

```php
protected $password = NULL;
```

### $port

```php
protected $port = NULL;
```

### $shouldIsDirectoryReturnTrue

```php
public $shouldIsDirectoryReturnTrue = FALSE;
```

```text
This is for testing the CopyRecursive logic.
```

## Methods (derived index)

- [__construct()](TestFileTransfer/__construct.md)
- [factory()](TestFileTransfer/factory.md)
- [connect()](TestFileTransfer/connect.md)
- [copyFileJailed()](TestFileTransfer/copyFileJailed.md)
- [removeDirectoryJailed()](TestFileTransfer/removeDirectoryJailed.md)
- [createDirectoryJailed()](TestFileTransfer/createDirectoryJailed.md)
- [removeFileJailed()](TestFileTransfer/removeFileJailed.md)
- [isDirectory()](TestFileTransfer/isDirectory.md)
- [isFile()](TestFileTransfer/isFile.md)
- [chmodJailed()](TestFileTransfer/chmodJailed.md)

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
