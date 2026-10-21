# aggregator_form_feed()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 66–133 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L66-L133)
- **Module/theme:** aggregator
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function aggregator_form_feed($form, &$form_state, stdClass $feed = NULL)
```

## Documentation

```text
Form constructor for adding and editing feed sources.

@param $feed
  (optional) If editing a feed, the feed to edit as a PHP stdClass value; if
  adding a new feed, NULL. Defaults to NULL.

@ingroup forms
@see aggregator_form_feed_validate()
@see aggregator_form_feed_submit()
```

## Code

```php
function aggregator_form_feed($form, &$form_state, stdClass $feed = NULL) {
  $period = drupal_map_assoc(array(900, 1800, 3600, 7200, 10800, 21600, 32400, 43200, 64800, 86400, 172800, 259200, 604800, 1209600, 2419200), 'format_interval');
  $period[AGGREGATOR_CLEAR_NEVER] = t('Never');

  $form['title'] = array('#type' => 'textfield',
    '#title' => t('Title'),
    '#default_value' => isset($feed->title) ? $feed->title : '',
    '#maxlength' => 255,
    '#description' => t('The name of the feed (or the name of the website providing the feed).'),
    '#required' => TRUE,
  );
  $form['url'] = array('#type' => 'textfield',
    '#title' => t('URL'),
    '#default_value' => isset($feed->url) ? $feed->url : '',
    '#maxlength' => NULL,
    '#description' => t('The fully-qualified URL of the feed.'),
    '#required' => TRUE,
  );
  $form['refresh'] = array('#type' => 'select',
    '#title' => t('Update interval'),
    '#default_value' => isset($feed->refresh) ? $feed->refresh : 3600,
    '#options' => $period,
    '#description' => t('The length of time between feed updates. Requires a correctly configured <a href="@cron">cron maintenance task</a>.', array('@cron' => url('admin/reports/status'))),
  );
  $form['block'] = array('#type' => 'select',
    '#title' => t('News items in block'),
    '#default_value' => isset($feed->block) ? $feed->block : 5,
    '#options' => drupal_map_assoc(array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)),
    '#description' => t("Drupal can make a block with the most recent news items of this feed. You can <a href=\"@block-admin\">configure blocks</a> to be displayed in the sidebar of your page. This setting lets you configure the number of news items to show in this feed's block. If you choose '0' this feed's block will be disabled.", array('@block-admin' => url('admin/structure/block'))),
  );

  // Handling of categories.
  $options = array();
  $values = array();
  $categories = db_query('SELECT c.cid, c.title, f.fid FROM {aggregator_category} c LEFT JOIN {aggregator_category_feed} f ON c.cid = f.cid AND f.fid = :fid ORDER BY title', array(':fid' => isset($feed->fid) ? $feed->fid : NULL));
  foreach ($categories as $category) {
    $options[$category->cid] = check_plain($category->title);
    if ($category->fid) $values[] = $category->cid;
  }

  if ($options) {
    $form['category'] = array(
      '#type' => 'checkboxes',
      '#title' => t('Categorize news items'),
      '#default_value' => $values,
      '#options' => $options,
      '#description' => t('New feed items are automatically filed in the checked categories.'),
    );
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );
  if (!empty($feed->fid)) {
    $form['actions']['delete'] = array(
      '#type' => 'submit',
      '#value' => t('Delete'),
    );
    $form['fid'] = array(
      '#type' => 'hidden',
      '#value' => $feed->fid,
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
