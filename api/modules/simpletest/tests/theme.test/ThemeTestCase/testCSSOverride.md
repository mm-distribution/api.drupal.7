# ThemeTestCase::testCSSOverride()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 97–113 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L97-L113)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCSSOverride()
```

## Documentation

```text
Ensures a theme's .info file is able to override a module CSS file from being added to the page.

@see test_theme.info
```

## Code

```php
  function testCSSOverride() {
    // Reuse the same page as in testPreprocessForSuggestions(). We're testing
    // what is output to the HTML HEAD based on what is in a theme's .info file,
    // so it doesn't matter what page we get, as long as it is themed with the
    // test theme. First we test with CSS aggregation disabled.
    variable_set('preprocess_css', 0);
    $this->drupalGet('theme-test/suggestion');
    $this->assertNoText('system.base.css', 'The theme\'s .info file is able to override a module CSS file from being added to the page.');

    // Also test with aggregation enabled, simply ensuring no PHP errors are
    // triggered during drupal_build_css_cache() when a source file doesn't
    // exist. Then allow remaining tests to continue with aggregation disabled
    // by default.
    variable_set('preprocess_css', 1);
    $this->drupalGet('theme-test/suggestion');
    variable_set('preprocess_css', 0);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
