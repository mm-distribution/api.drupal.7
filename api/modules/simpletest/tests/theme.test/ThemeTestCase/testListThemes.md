# ThemeTestCase::testListThemes()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 131–147 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L131-L147)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testListThemes()
```

## Documentation

```text
Test the list_themes() function.
```

## Code

```php
  function testListThemes() {
    $themes = list_themes();
    // Check if drupal_theme_access() retrieves enabled themes properly from list_themes().
    $this->assertTrue(drupal_theme_access('test_theme'), 'Enabled theme detected');
    // Check if list_themes() returns disabled themes.
    $this->assertTrue(array_key_exists('test_basetheme', $themes), 'Disabled theme detected');
    // Check for base theme and subtheme lists.
    $base_theme_list = array('test_basetheme' => 'Theme test base theme');
    $sub_theme_list = array('test_subtheme' => 'Theme test subtheme');
    $this->assertIdentical($themes['test_basetheme']->sub_themes, $sub_theme_list, 'Base theme\'s object includes list of subthemes.');
    $this->assertIdentical($themes['test_subtheme']->base_themes, $base_theme_list, 'Subtheme\'s object includes list of base themes.');
    // Check for theme engine in subtheme.
    $this->assertIdentical($themes['test_subtheme']->engine, 'phptemplate', 'Subtheme\'s object includes the theme engine.');
    // Check for theme engine prefix.
    $this->assertIdentical($themes['test_basetheme']->prefix, 'phptemplate', 'Base theme\'s object includes the theme engine prefix.');
    $this->assertIdentical($themes['test_subtheme']->prefix, 'phptemplate', 'Subtheme\'s object includes the theme engine prefix.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
