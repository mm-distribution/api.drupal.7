# aggregator_form_opml()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 250–295 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L250-L295)
- **Module/theme:** aggregator
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function aggregator_form_opml($form, &$form_state)
```

## Documentation

```text
Form constructor for importing feeds from OPML.

@ingroup forms
@see aggregator_form_opml_validate()
@see aggregator_form_opml_submit()
```

## Code

```php
function aggregator_form_opml($form, &$form_state) {
  $period = drupal_map_assoc(array(900, 1800, 3600, 7200, 10800, 21600, 32400, 43200, 64800, 86400, 172800, 259200, 604800, 1209600, 2419200), 'format_interval');

  $form['upload'] = array(
    '#type' => 'file',
    '#title' => t('OPML File'),
    '#description' => t('Upload an OPML file containing a list of feeds to be imported.'),
  );
  $form['remote'] = array(
    '#type' => 'textfield',
    '#title' => t('OPML Remote URL'),
    '#maxlength' => 1024,
    '#description' => t('Enter the URL of an OPML file. This file will be downloaded and processed only once on submission of the form.'),
  );
  $form['refresh'] = array(
    '#type' => 'select',
    '#title' => t('Update interval'),
    '#default_value' => 3600,
    '#options' => $period,
    '#description' => t('The length of time between feed updates. Requires a correctly configured <a href="@cron">cron maintenance task</a>.', array('@cron' => url('admin/reports/status'))),
  );
  $form['block'] = array('#type' => 'select',
    '#title' => t('News items in block'),
    '#default_value' => 5,
    '#options' => drupal_map_assoc(array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)),
    '#description' => t("Drupal can make a block with the most recent news items of a feed. You can <a href=\"@block-admin\">configure blocks</a> to be displayed in the sidebar of your page. This setting lets you configure the number of news items to show in a feed's block. If you choose '0' these feeds' blocks will be disabled.", array('@block-admin' => url('admin/structure/block'))),
  );

  // Handling of categories.
  $options = array_map('check_plain', db_query("SELECT cid, title FROM {aggregator_category} ORDER BY title")->fetchAllKeyed());
  if ($options) {
    $form['category'] = array(
      '#type' => 'checkboxes',
      '#title' => t('Categorize news items'),
      '#options' => $options,
      '#description' => t('New feed items are automatically filed in the checked categories.'),
    );
  }
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Import')
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
