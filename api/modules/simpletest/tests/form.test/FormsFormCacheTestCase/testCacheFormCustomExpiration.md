# FormsFormCacheTestCase::testCacheFormCustomExpiration()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1583–1599 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1583-L1599)
- **Class:** [FormsFormCacheTestCase](../FormsFormCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCacheFormCustomExpiration()
```

## Documentation

```text
Tests changing form_cache_expiration.
```

## Code

```php
  function testCacheFormCustomExpiration() {
    variable_set('form_cache_expiration', -1 * (24 * 60 * 60));

    $form = drupal_get_form('form_test_cache_form');
    $form_state = array('foo' => 'bar', 'build_info' => array('baz'));
    form_set_cache($form['#build_id'], $form, $form_state);

    // Clear expired entries from cache_form, which should include the entry we
    // just stored. Without this, the form will still be retrieved from cache.
    cache_clear_all(NULL, 'cache_form');

    $cached_form_state = array();
    $cached_form = form_get_cache($form['#build_id'], $cached_form_state);

    $this->assertNull($cached_form, 'Expired form was not returned from cache.');
    $this->assertTrue(empty($cached_form_state), 'No data retrieved from cache for expired form.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
