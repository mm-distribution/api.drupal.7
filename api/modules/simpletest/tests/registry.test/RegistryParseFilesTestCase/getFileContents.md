# RegistryParseFilesTestCase::getFileContents()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 136–146 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L136-L146)
- **Class:** [RegistryParseFilesTestCase](../RegistryParseFilesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function getFileContents($fileType)
```

## Documentation

```text
getFileContents
```

## Code

```php
  function getFileContents($fileType) {
    $file_contents = <<<CONTENTS
<?php

class {$this->$fileType->className} {}

interface {$this->$fileType->interfaceName} {}

CONTENTS;
    return $file_contents;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
