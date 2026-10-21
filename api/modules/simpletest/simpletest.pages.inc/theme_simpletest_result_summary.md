# theme_simpletest_result_summary()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 379–382 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L379-L382)
- **Module/theme:** simpletest
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_simpletest_result_summary($variables)
```

## Documentation

```text
Returns HTML for the summary status of a simpletest result.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_simpletest_result_summary($variables) {
  $form = $variables['form'];
  return '<div class="simpletest-' . ($form['#ok'] ? 'pass' : 'fail') . '">' . _simpletest_format_summary_line($form) . '</div>';
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
