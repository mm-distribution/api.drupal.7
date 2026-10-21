# theme_trigger_display()

- **Type:** Function
- **File:** [`modules/trigger/trigger.admin.inc`](_file.md), lines 296–319 · [local source](../../../../source/modules/trigger/trigger.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc#L296-L319)
- **Module/theme:** trigger
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_trigger_display($variables)
```

## Documentation

```text
Returns HTML for the form showing actions assigned to a trigger.

@param $variables
  An associative array containing:
  - element: The fieldset including all assigned actions.

@ingroup themeable
```

## Code

```php
function theme_trigger_display($variables) {
  $element = $variables['element'];

  $header = array();
  $rows = array();
  if (isset($element['assigned']) && count($element['assigned']['#value'])) {
    $header = array(array('data' => t('Name')), array('data' => t('Operation')));
    $rows = array();
    foreach ($element['assigned']['#value'] as $aid => $info) {
      $rows[] = array(
        check_plain($info['label']),
        $info['link']
      );
    }
  }

  if (count($rows)) {
    $output = theme('table', array('header' => $header, 'rows' => $rows)) . drupal_render_children($element);
  }
  else {
    $output = drupal_render_children($element);
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
