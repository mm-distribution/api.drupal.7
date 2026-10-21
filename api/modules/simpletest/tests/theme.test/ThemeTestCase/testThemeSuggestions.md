# ThemeTestCase::testThemeSuggestions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 30–52 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L30-L52)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeSuggestions()
```

## Documentation

```text
Test function theme_get_suggestions() for SA-CORE-2009-003.
```

## Code

```php
  function testThemeSuggestions() {
    // Set the front page as something random otherwise the CLI
    // test runner fails.
    variable_set('site_frontpage', 'nobody-home');
    $args = array('node', '1', 'edit');
    $suggestions = theme_get_suggestions($args, 'page');
    $this->assertEqual($suggestions, array('page__node', 'page__node__%', 'page__node__1', 'page__node__edit'), 'Found expected node edit page suggestions');
    // Check attack vectors.
    $args = array('node', '\\1');
    $suggestions = theme_get_suggestions($args, 'page');
    $this->assertEqual($suggestions, array('page__node', 'page__node__%', 'page__node__1'), 'Removed invalid \\ from suggestions');
    $args = array('node', '1/');
    $suggestions = theme_get_suggestions($args, 'page');
    $this->assertEqual($suggestions, array('page__node', 'page__node__%', 'page__node__1'), 'Removed invalid / from suggestions');
    $args = array('node', "1\0");
    $suggestions = theme_get_suggestions($args, 'page');
    $this->assertEqual($suggestions, array('page__node', 'page__node__%', 'page__node__1'), 'Removed invalid \\0 from suggestions');
    // Define path with hyphens to be used to generate suggestions.
    $args = array('node', '1', 'hyphen-path');
    $result = array('page__node', 'page__node__%', 'page__node__1', 'page__node__hyphen_path');
    $suggestions = theme_get_suggestions($args, 'page');
    $this->assertEqual($suggestions, $result, 'Found expected page suggestions for paths containing hyphens.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
