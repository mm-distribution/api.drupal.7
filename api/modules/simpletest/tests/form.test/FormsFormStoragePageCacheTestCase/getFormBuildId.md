# FormsFormStoragePageCacheTestCase::getFormBuildId()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1472–1476 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1472-L1476)
- **Class:** [FormsFormStoragePageCacheTestCase](../FormsFormStoragePageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function getFormBuildId()
```

## Documentation

```text
Return the build id of the current form.
```

## Code

```php
  protected function getFormBuildId() {
    $build_id_fields = $this->xpath('//input[@name="form_build_id"]');
    $this->assertEqual(count($build_id_fields), 1, 'One form build id field on the page');
    return (string) $build_id_fields[0]['value'];
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
