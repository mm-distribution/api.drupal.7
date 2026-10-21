# theme_aggregator_categorize_items()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 282–300 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L282-L300)
- **Module/theme:** aggregator
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_aggregator_categorize_items($variables)
```

## Documentation

```text
Returns HTML for the aggregator page list form for assigning categories.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_aggregator_categorize_items($variables) {
  $form = $variables['form'];

  $output = drupal_render($form['feed_source']);
  $rows = array();
  if (!empty($form['items'])) {
    foreach (element_children($form['items']) as $key) {
      $rows[] = array(
        drupal_render($form['items'][$key]),
        array('data' => drupal_render($form['categories'][$key]), 'class' => array('categorize-item')),
      );
    }
  }
  $output .= theme('table', array('header' => array('', t('Categorize')), 'rows' => $rows));
  $output .= drupal_render($form['submit']);
  $output .= drupal_render_children($form);

  return theme('aggregator_wrapper', array('content' => $output));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
