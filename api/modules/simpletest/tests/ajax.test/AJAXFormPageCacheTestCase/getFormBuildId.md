# AJAXFormPageCacheTestCase::getFormBuildId()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 535–539 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L535-L539)
- **Class:** [AJAXFormPageCacheTestCase](../AJAXFormPageCacheTestCase.md)
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
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
