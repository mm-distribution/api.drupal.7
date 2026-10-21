# form_process_date()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3097–3148 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3097-L3148)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_date($element)
```

## Documentation

```text
Expands a date element into year, month, and day select elements.
```

## Code

```php
function form_process_date($element) {
  // Default to current date
  if (empty($element['#value'])) {
    $element['#value'] = array(
      'day' => format_date(REQUEST_TIME, 'custom', 'j'),
      'month' => format_date(REQUEST_TIME, 'custom', 'n'),
      'year' => format_date(REQUEST_TIME, 'custom', 'Y'),
    );
  }

  $element['#tree'] = TRUE;

  // Determine the order of day, month, year in the site's chosen date format.
  $format = variable_get('date_format_short', 'm/d/Y - H:i');
  $sort = array();
  $sort['day'] = max(strpos($format, 'd'), strpos($format, 'j'));
  $sort['month'] = max(strpos($format, 'm'), strpos($format, 'M'));
  $sort['year'] = strpos($format, 'Y');
  asort($sort);
  $order = array_keys($sort);

  // Output multi-selector for date.
  foreach ($order as $type) {
    switch ($type) {
      case 'day':
        $options = drupal_map_assoc(range(1, 31));
        $title = t('Day');
        break;

      case 'month':
        $options = drupal_map_assoc(range(1, 12), 'map_month');
        $title = t('Month');
        break;

      case 'year':
        $options = drupal_map_assoc(range(1900, 2050));
        $title = t('Year');
        break;
    }

    $element[$type] = array(
      '#type' => 'select',
      '#title' => $title,
      '#title_display' => 'invisible',
      '#value' => $element['#value'][$type],
      '#attributes' => $element['#attributes'],
      '#options' => $options,
    );
  }

  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
