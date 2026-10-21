# aggregator_categorize_items()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 205–243 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L205-L243)
- **Module/theme:** aggregator
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function aggregator_categorize_items($items, $feed_source = '')
```

## Documentation

```text
Form constructor to build the page list form.

@param $items
  An array of the feed items.
@param $feed_source
  (optional) The feed source URL. Defaults to an empty string.

@return array
  An array of FAPI elements.

@see aggregator_categorize_items_submit()
@see theme_aggregator_categorize_items()
@ingroup forms
```

## Code

```php
function aggregator_categorize_items($items, $feed_source = '') {
  $form['#submit'][] = 'aggregator_categorize_items_submit';
  $form['#theme'] = 'aggregator_categorize_items';
  $form['feed_source'] = array(
    '#value' => $feed_source,
  );
  $categories = array();
  $done = FALSE;
  $form['items'] = array();
  $form['categories'] = array(
    '#tree' => TRUE,
  );
  foreach ($items as $item) {
    $form['items'][$item->iid] = array('#markup' => theme('aggregator_item', array('item' => $item)));
    $form['categories'][$item->iid] = array();
    $categories_result = db_query('SELECT c.cid, c.title, ci.iid FROM {aggregator_category} c LEFT JOIN {aggregator_category_item} ci ON c.cid = ci.cid AND ci.iid = :iid', array(':iid' => $item->iid));
    $selected = array();
    foreach ($categories_result as $category) {
      if (!$done) {
        $categories[$category->cid] = check_plain($category->title);
      }
      if ($category->iid) {
        $selected[] = $category->cid;
      }
    }
    $done = TRUE;
    $form['categories'][$item->iid] = array(
      '#type' => variable_get('aggregator_category_selector', 'checkboxes'),
      '#default_value' => $selected,
      '#options' => $categories,
      '#size' => 10,
      '#multiple' => TRUE
    );
  }
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save categories'));

  return $form;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
