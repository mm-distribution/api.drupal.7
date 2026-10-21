# FormsFileInclusionTestCase::testLoadMenuInclude()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2186–2189 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2186-L2189)
- **Class:** [FormsFileInclusionTestCase](../FormsFileInclusionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLoadMenuInclude()
```

## Documentation

```text
Tests loading an include specified in hook_menu().
```

## Code

```php
  function testLoadMenuInclude() {
    $this->drupalPostAJAX('form-test/load-include-menu', array(), array('op' => t('Save')), 'system/ajax', array(), array(), 'form-test-load-include-menu');
    $this->assertText('Submit callback called.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
