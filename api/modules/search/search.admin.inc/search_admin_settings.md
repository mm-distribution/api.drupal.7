# search_admin_settings()

- **Type:** Function
- **File:** [`modules/search/search.admin.inc`](_file.md), lines 52–150 · [local source](../../../../source/modules/search/search.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc#L52-L150)
- **Module/theme:** search
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function search_admin_settings($form)
```

## Documentation

```text
Menu callback: displays the search module settings page.

@ingroup forms

@see search_admin_settings_validate()
@see search_admin_settings_submit()
@see search_admin_reindex_submit()
```

## Code

```php
function search_admin_settings($form) {
  // Collect some stats
  $remaining = 0;
  $total = 0;
  foreach (variable_get('search_active_modules', array('node', 'user')) as $module) {
    if ($status = module_invoke($module, 'search_status')) {
      $remaining += $status['remaining'];
      $total += $status['total'];
    }
  }

  $count = format_plural($remaining, 'There is 1 item left to index.', 'There are @count items left to index.');
  $percentage = ((int)min(100, 100 * ($total - $remaining) / max(1, $total))) . '%';
  $status = '<p><strong>' . t('%percentage of the site has been indexed.', array('%percentage' => $percentage)) . ' ' . $count . '</strong></p>';
  $form['status'] = array('#type' => 'fieldset', '#title' => t('Indexing status'));
  $form['status']['status'] = array('#markup' => $status);
  $form['status']['wipe'] = array('#type' => 'submit', '#value' => t('Re-index site'), '#submit' => array('search_admin_reindex_submit'));

  $items = drupal_map_assoc(array(10, 20, 50, 100, 200, 500));

  // Indexing throttle:
  $form['indexing_throttle'] = array(
    '#type' => 'fieldset',
    '#title' => t('Indexing throttle')
  );
  $form['indexing_throttle']['search_cron_limit'] = array(
    '#type' => 'select',
    '#title' => t('Number of items to index per cron run'),
    '#default_value' => variable_get('search_cron_limit', 100),
    '#options' => $items,
    '#description' => t('The maximum number of items indexed in each pass of a <a href="@cron">cron maintenance task</a>. If necessary, reduce the number of items to prevent timeouts and memory errors while indexing.', array('@cron' => url('admin/reports/status')))
  );
  // Indexing settings:
  $form['indexing_settings'] = array(
    '#type' => 'fieldset',
    '#title' => t('Indexing settings')
  );
  $form['indexing_settings']['info'] = array(
    '#markup' => t('<p><em>Changing the settings below will cause the site index to be rebuilt. The search index is not cleared but systematically updated to reflect the new settings. Searching will continue to work but new content won\'t be indexed until all existing content has been re-indexed.</em></p><p><em>The default settings should be appropriate for the majority of sites.</em></p>')
  );
  $form['indexing_settings']['minimum_word_size'] = array(
    '#type' => 'textfield',
    '#title' => t('Minimum word length to index'),
    '#default_value' => variable_get('minimum_word_size', 3),
    '#size' => 5,
    '#maxlength' => 3,
    '#description' => t('The number of characters a word has to be to be indexed. A lower setting means better search result ranking, but also a larger database. Each search query must contain at least one keyword that is this size (or longer).'),
    '#element_validate' => array('element_validate_integer_positive'),
  );
  $form['indexing_settings']['overlap_cjk'] = array(
    '#type' => 'checkbox',
    '#title' => t('Simple CJK handling'),
    '#default_value' => variable_get('overlap_cjk', TRUE),
    '#description' => t('Whether to apply a simple Chinese/Japanese/Korean tokenizer based on overlapping sequences. Turn this off if you want to use an external preprocessor for this instead. Does not affect other languages.')
  );

  $form['active'] = array(
    '#type' => 'fieldset',
    '#title' => t('Active search modules')
  );
  $module_options = _search_get_module_names();
  $form['active']['search_active_modules'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Active modules'),
    '#title_display' => 'invisible',
    '#default_value' => variable_get('search_active_modules', array('node', 'user')),
    '#options' => $module_options,
    '#description' => t('Choose which search modules are active from the available modules.')
  );
  $form['active']['search_default_module'] = array(
    '#title' => t('Default search module'),
    '#type' => 'radios',
    '#default_value' => variable_get('search_default_module', 'node'),
    '#options' => $module_options,
    '#description' => t('Choose which search module is the default.')
  );
  $form['logging'] = array(
    '#type' => 'fieldset',
    '#title' => t('Logging')
  );
  $form['logging']['search_logging'] = array(
    '#type' => 'checkbox',
    '#title' => t('Log searches'),
    '#default_value' => variable_get('search_logging', 1),
    '#description' => t('If checked, all searches will be logged. Uncheck to skip logging. Logging may affect performance.'),
  );
  $form['#validate'][] = 'search_admin_settings_validate';
  $form['#submit'][] = 'search_admin_settings_submit';

  // Per module settings
  foreach (variable_get('search_active_modules', array('node', 'user')) as $module) {
    $added_form = module_invoke($module, 'search_admin');
    if (is_array($added_form)) {
      $form = array_merge($form, $added_form);
    }
  }

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/search/search.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/search/search.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
