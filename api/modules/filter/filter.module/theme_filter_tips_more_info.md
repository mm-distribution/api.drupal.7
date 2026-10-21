# theme_filter_tips_more_info()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1198–1200 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1198-L1200)
- **Module/theme:** filter
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_filter_tips_more_info()
```

## Documentation

```text
Returns HTML for a link to the more extensive filter tips.

@ingroup themeable
```

## Code

```php
function theme_filter_tips_more_info() {
  return '<p>' . l(t('More information about text formats'), 'filter/tips', array('attributes' => array('target' => '_blank'))) . '</p>';
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
