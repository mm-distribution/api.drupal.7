# ThemeTestCase::testPreprocessForSuggestions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 61–68 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L61-L68)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testPreprocessForSuggestions()
```

## Documentation

```text
Ensures preprocess functions run even for suggestion implementations.

The theme hook used by this test has its base preprocess function in a
separate file, so this test also ensures that that file is correctly loaded
when needed.
```

## Code

```php
  function testPreprocessForSuggestions() {
    // Test with both an unprimed and primed theme registry.
    drupal_theme_rebuild();
    for ($i = 0; $i < 2; $i++) {
      $this->drupalGet('theme-test/suggestion');
      $this->assertText('Theme hook implementor=test_theme_theme_test__suggestion(). Foo=template_preprocess_theme_test', 'Theme hook suggestion ran with data available from a preprocess function for the base hook.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
