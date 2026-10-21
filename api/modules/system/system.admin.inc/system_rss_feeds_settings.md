# system_rss_feeds_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1906–1929 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1906-L1929)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_rss_feeds_settings()
```

## Documentation

```text
Form builder; Configure how the site handles RSS feeds.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_rss_feeds_settings() {
  $form['feed_description'] = array(
    '#type' => 'textarea',
    '#title' => t('Feed description'),
    '#default_value' => variable_get('feed_description', ''),
    '#description' => t('Description of your site, included in each feed.')
  );
  $form['feed_default_items'] = array(
    '#type' => 'select',
    '#title' => t('Number of items in each feed'),
    '#default_value' => variable_get('feed_default_items', 10),
    '#options' => drupal_map_assoc(array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30)),
    '#description' => t('Default number of items to include in each feed.')
  );
  $form['feed_item_length'] = array(
    '#type' => 'select',
    '#title' => t('Feed content'),
    '#default_value' => variable_get('feed_item_length', 'fulltext'),
    '#options' => array('title' => t('Titles only'), 'teaser' => t('Titles plus teaser'), 'fulltext' => t('Full text')),
    '#description' => t('Global setting for the default display of content items in each feed.')
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
