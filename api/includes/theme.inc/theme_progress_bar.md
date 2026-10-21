# theme_progress_bar()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2393–2401 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2393-L2401)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_progress_bar($variables)
```

## Documentation

```text
Returns HTML for a progress bar.

Note that the core Batch API uses this only for non-JavaScript batch jobs.

@param $variables
  An associative array containing:
  - percent: The percentage of the progress.
  - message: A string containing information to be displayed.
```

## Code

```php
function theme_progress_bar($variables) {
  $output = '<div id="progress" class="progress">';
  $output .= '<div class="bar"><div class="filled" style="width: ' . $variables['percent'] . '%"></div></div>';
  $output .= '<div class="percentage">' . $variables['percent'] . '%</div>';
  $output .= '<div class="message">' . $variables['message'] . '</div>';
  $output .= '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
