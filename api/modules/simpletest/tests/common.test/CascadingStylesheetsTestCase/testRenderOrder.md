# CascadingStylesheetsTestCase::testRenderOrder()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 922–950 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L922-L950)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderOrder()
```

## Documentation

```text
Test CSS ordering.
```

## Code

```php
  function testRenderOrder() {
    // A module CSS file.
    drupal_add_css(drupal_get_path('module', 'simpletest') . '/simpletest.css');
    // A few system CSS files, ordered in a strange way.
    $system_path = drupal_get_path('module', 'system');
    drupal_add_css($system_path . '/system.menus.css', array('group' => CSS_SYSTEM));
    drupal_add_css($system_path . '/system.base.css', array('group' => CSS_SYSTEM, 'weight' => -10));
    drupal_add_css($system_path . '/system.theme.css', array('group' => CSS_SYSTEM));

    $expected = array(
      $system_path . '/system.base.css',
      $system_path . '/system.menus.css',
      $system_path . '/system.theme.css',
      drupal_get_path('module', 'simpletest') . '/simpletest.css',
    );


    $styles = drupal_get_css();
    // Stylesheet URL may be the href of a LINK tag or in an @import statement
    // of a STYLE tag.
    if (preg_match_all('/(href="|url\(")' . preg_quote($GLOBALS['base_url'] . '/', '/') . '([^?]+)\?/', $styles, $matches)) {
      $result = $matches[2];
    }
    else {
      $result = array();
    }

    $this->assertIdentical($result, $expected, 'The CSS files are in the expected order.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
