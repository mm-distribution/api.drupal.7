# FormsFormCacheTestCase::testCacheForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1568–1578 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1568-L1578)
- **Class:** [FormsFormCacheTestCase](../FormsFormCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCacheForm()
```

## Documentation

```text
Tests storing and retrieving the form from cache.
```

## Code

```php
  function testCacheForm() {
    $form = drupal_get_form('form_test_cache_form');
    $form_state = array('foo' => 'bar', 'build_info' => array('baz'));
    form_set_cache($form['#build_id'], $form, $form_state);

    $cached_form_state = array();
    $cached_form = form_get_cache($form['#build_id'], $cached_form_state);

    $this->assertEqual($cached_form['#build_id'], $form['#build_id'], 'Form retrieved from cache_form successfully.');
    $this->assertEqual($cached_form_state['foo'], 'bar', 'Data retrieved from cache_form successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
