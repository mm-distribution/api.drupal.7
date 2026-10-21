# DrupalDummyStreamWrapper::getInternalUri()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file_test.module`](../_file.md), lines 444–446 · [local source](../../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L444-L446)
- **Class:** [DrupalDummyStreamWrapper](../DrupalDummyStreamWrapper.md)
- **Module/theme:** batch_test

## Signature

```php
function getInternalUri()
```

## Documentation

```text
Override getInternalUri().

Return a dummy path for testing.
```

## Code

```php
  function getInternalUri() {
    return '/dummy/example.txt';
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
