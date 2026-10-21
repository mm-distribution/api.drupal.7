# DrupalDummyStreamWrapper::getDirectoryPath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file_test.module`](../_file.md), lines 435–437 · [local source](../../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L435-L437)
- **Class:** [DrupalDummyStreamWrapper](../DrupalDummyStreamWrapper.md)
- **Module/theme:** batch_test

## Signature

```php
function getDirectoryPath()
```

## Documentation

_No docblock in source._

## Code

```php
  function getDirectoryPath() {
    return variable_get('stream_public_path', 'sites/default/files');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
