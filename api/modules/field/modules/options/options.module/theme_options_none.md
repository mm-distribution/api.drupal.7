# theme_options_none()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 409–425 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L409-L425)
- **Module/theme:** options
- **Topics:** [themeable](../../../../../topics/themeable.md)

## Signature

```php
function theme_options_none($variables)
```

## Documentation

```text
Returns HTML for the label for the empty value for options that are not required.

The default theme will display N/A for a radio list and '- None -' for a select.

@param $variables
  An associative array containing:
  - instance: An array representing the widget requesting the options.

@ingroup themeable
```

## Code

```php
function theme_options_none($variables) {
  $instance = $variables['instance'];
  $option = $variables['option'];

  $output = '';
  switch ($instance['widget']['type']) {
    case 'options_buttons':
      $output = t('N/A');
      break;

    case 'options_select':
      $output = ($option == 'option_none' ? t('- None -') : t('- Select a value -'));
      break;
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
