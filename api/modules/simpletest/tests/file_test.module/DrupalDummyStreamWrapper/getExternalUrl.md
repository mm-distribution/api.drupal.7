# DrupalDummyStreamWrapper::getExternalUrl()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file_test.module`](../_file.md), lines 453–455 · [local source](../../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L453-L455)
- **Class:** [DrupalDummyStreamWrapper](../DrupalDummyStreamWrapper.md)
- **Module/theme:** batch_test

## Signature

```php
function getExternalUrl()
```

## Documentation

```text
Override getExternalUrl().

Return the HTML URI of a public file.
```

## Code

```php
  function getExternalUrl() {
    return '/dummy/example.txt';
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
