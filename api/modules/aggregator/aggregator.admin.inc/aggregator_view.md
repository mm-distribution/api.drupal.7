# aggregator_view()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 21–53 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L21-L53)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_view()
```

## Documentation

```text
Displays the aggregator administration page.

@return
  A HTML-formatted string with administration page content.
```

## Code

```php
function aggregator_view() {
  $result = db_query('SELECT f.fid, f.title, f.url, f.refresh, f.checked, f.link, f.description, f.hash, f.etag, f.modified, f.image, f.block, COUNT(i.iid) AS items FROM {aggregator_feed} f LEFT JOIN {aggregator_item} i ON f.fid = i.fid GROUP BY f.fid, f.title, f.url, f.refresh, f.checked, f.link, f.description, f.hash, f.etag, f.modified, f.image, f.block ORDER BY f.title');

  $output = '<h3>' . t('Feed overview') . '</h3>';

  $header = array(t('Title'), t('Items'), t('Last update'), t('Next update'), array('data' => t('Operations'), 'colspan' => '3'));
  $rows = array();
  foreach ($result as $feed) {
    $rows[] = array(
      l($feed->title, "aggregator/sources/$feed->fid"),
      format_plural($feed->items, '1 item', '@count items'),
      ($feed->checked ? t('@time ago', array('@time' => format_interval(REQUEST_TIME - $feed->checked))) : t('never')),
      ($feed->checked && $feed->refresh ? t('%time left', array('%time' => format_interval($feed->checked + $feed->refresh - REQUEST_TIME))) : t('never')),
      l(t('edit'), "admin/config/services/aggregator/edit/feed/$feed->fid"),
      l(t('remove items'), "admin/config/services/aggregator/remove/$feed->fid"),
      l(t('update items'), "admin/config/services/aggregator/update/$feed->fid", array('query' => array('token' => drupal_get_token("aggregator/update/$feed->fid")))),
    );
  }
  $output .= theme('table', array('header' => $header, 'rows' => $rows, 'empty' => t('No feeds available. <a href="@link">Add feed</a>.', array('@link' => url('admin/config/services/aggregator/add/feed')))));

  $result = db_query('SELECT c.cid, c.title, COUNT(ci.iid) as items FROM {aggregator_category} c LEFT JOIN {aggregator_category_item} ci ON c.cid = ci.cid GROUP BY c.cid, c.title ORDER BY title');

  $output .= '<h3>' . t('Category overview') . '</h3>';

  $header = array(t('Title'), t('Items'), t('Operations'));
  $rows = array();
  foreach ($result as $category) {
    $rows[] = array(l($category->title, "aggregator/categories/$category->cid"), format_plural($category->items, '1 item', '@count items'), l(t('edit'), "admin/config/services/aggregator/edit/category/$category->cid"));
  }
  $output .= theme('table', array('header' => $header, 'rows' => $rows, 'empty' => t('No categories available. <a href="@link">Add category</a>.', array('@link' => url('admin/config/services/aggregator/add/category')))));

  return $output;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
