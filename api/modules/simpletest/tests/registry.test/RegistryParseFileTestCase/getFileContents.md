# RegistryParseFileTestCase::getFileContents()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 38–48 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L38-L48)
- **Class:** [RegistryParseFileTestCase](../RegistryParseFileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function getFileContents()
```

## Documentation

```text
getFileContents
```

## Code

```php
  function getFileContents() {
    $file_contents = <<<CONTENTS
<?php

class {$this->className} {}

interface {$this->interfaceName} {}

CONTENTS;
    return $file_contents;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
