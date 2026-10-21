# ThemeTestCase::testFrontPageThemeSuggestion()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 73–82 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L73-L82)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFrontPageThemeSuggestion()
```

## Documentation

```text
Ensure page-front template suggestion is added when on front page.
```

## Code

```php
  function testFrontPageThemeSuggestion() {
    $q = $_GET['q'];
    // Set $_GET['q'] to node because theme_get_suggestions() will query it to
    // see if we are on the front page.
    $_GET['q'] = variable_get('site_frontpage', 'node');
    $suggestions = theme_get_suggestions(explode('/', $_GET['q']), 'page');
    // Set it back to not annoy the batch runner.
    $_GET['q'] = $q;
    $this->assertTrue(in_array('page__front', $suggestions), 'Front page template was suggested.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
