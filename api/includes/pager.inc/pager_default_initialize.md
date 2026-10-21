# pager_default_initialize()

- **Type:** Function
- **File:** [`includes/pager.inc`](_file.md), lines 289–300 · [local source](../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L289-L300)

## Signature

```php
function pager_default_initialize($total, $limit, $element = 0)
```

## Documentation

```text
Initializes a pager for theme('pager').

This function sets up the necessary global variables so that future calls
to theme('pager') will render a pager that correctly corresponds to the
items being displayed.

If the items being displayed result from a database query performed using
Drupal's database API, and if you have control over the construction of the
database query, you do not need to call this function directly; instead, you
can simply extend the query object with the 'PagerDefault' extender before
executing it. For example:
@code
  $query = db_select('some_table')->extend('PagerDefault');
@endcode

However, if you are using a different method for generating the items to be
paged through, then you should call this function in preparation.

The following example shows how this function can be used in a page callback
that invokes an external datastore with an SQL-like syntax:
@code
  // First find the total number of items and initialize the pager.
  $where = "status = 1";
  $total = mymodule_select("SELECT COUNT(*) FROM data " . $where)->result();
  $num_per_page = variable_get('mymodule_num_per_page', 10);
  $page = pager_default_initialize($total, $num_per_page);

  // Next, retrieve and display the items for the current page.
  $offset = $num_per_page * $page;
  $result = mymodule_select("SELECT * FROM data " . $where . " LIMIT %d, %d", $offset, $num_per_page)->fetchAll();
  $output = theme('mymodule_results', array('result' => $result));

  // Finally, display the pager controls, and return.
  $output .= theme('pager');
  return $output;
@endcode

A second example involves a page callback that invokes an external search
service where the total number of matching results is provided as part of
the returned set (so that we do not need a separate query in order to obtain
this information). Here, we call pager_find_page() to calculate the desired
offset before the search is invoked:
@code
  // Perform the query, using the requested offset from pager_find_page().
  // This comes from a URL parameter, so here we are assuming that the URL
  // parameter corresponds to an actual page of results that will exist
  // within the set.
  $page = pager_find_page();
  $num_per_page = variable_get('mymodule_num_per_page', 10);
  $offset = $num_per_page * $page;
  $result = mymodule_remote_search($keywords, $offset, $num_per_page);

  // Now that we have the total number of results, initialize the pager.
  pager_default_initialize($result->total, $num_per_page);

  // Display the search results.
  $output = theme('search_results', array('results' => $result->data, 'type' => 'remote'));

  // Finally, display the pager controls, and return.
  $output .= theme('pager');
  return $output;
@endcode

@param $total
 The total number of items to be paged.
@param $limit
 The number of items the calling code will display per page.
@param $element
 An optional integer to distinguish between multiple pagers on one page.

@return
  The number of the current page, within the pager represented by $element.
  This is determined from the URL query parameter $_GET['page'], or 0 by
  default. However, if a page that does not correspond to the actual range
  of the result set was requested, this function will return the closest
  page actually within the result set.
```

## Code

```php
function pager_default_initialize($total, $limit, $element = 0) {
  global $pager_page_array, $pager_total, $pager_total_items, $pager_limits;

  $page = pager_find_page($element);

  // We calculate the total of pages as ceil(items / limit).
  $pager_total_items[$element] = $total;
  $pager_total[$element] = ceil($pager_total_items[$element] / $limit);
  $pager_page_array[$element] = max(0, min($page, ((int) $pager_total[$element]) - 1));
  $pager_limits[$element] = $limit;
  return $pager_page_array[$element];
}
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
