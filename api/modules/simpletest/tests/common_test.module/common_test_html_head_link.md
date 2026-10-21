# common_test_html_head_link()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 299–324 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L299-L324)
- **Module/theme:** batch_test

## Signature

```php
function common_test_html_head_link()
```

## Documentation

```text
Page callback.
```

## Code

```php
function common_test_html_head_link() {
  drupal_add_html_head_link(array(
    'href' => '/foo?bar=baz',
    'rel' => 'alternate',
  ), TRUE);
  drupal_add_html_head_link(array(
    'href' => '/not-added-to-http-headers',
    'rel' => 'alternate',
  ), FALSE);
  drupal_add_html_head_link(array(
    'href' => '/foo/bar',
    'hreflang' => 'nl',
    'rel' => 'alternate',
  ), TRUE);
  drupal_add_html_head_link(array(
    'href' => '/foo/bar',
    'hreflang' => 'de',
    'rel' => 'alternate',
  ), TRUE);
  drupal_add_html_head_link(array(
    'href' => '/foo?bar=baz&baz=false',
    'hreflang' => 'en',
    'rel' => 'alternate',
  ), TRUE);
  return '';
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
