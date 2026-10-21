# drupal_render_cache_by_query()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6526–6538 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6526-L6538)

## Signature

```php
function drupal_render_cache_by_query($query, $function, $expire = CACHE_TEMPORARY, $granularity = NULL)
```

## Documentation

```text
Prepares an element for caching based on a query.

This smart caching strategy saves Drupal from querying and rendering to HTML
when the underlying query is unchanged.

Expensive queries should use the query builder to create the query and then
call this function. Executing the query and formatting results should happen
in a #pre_render callback.

@param $query
  A select query object as returned by db_select().
@param $function
  The name of the function doing this caching. A _pre_render suffix will be
  added to this string and is also part of the cache key in
  drupal_render_cache_set() and drupal_render_cache_get().
@param $expire
  The cache expire time, passed eventually to cache_set().
@param $granularity
  One or more granularity constants passed to drupal_render_cid_parts().

@return
  A renderable array with the following keys and values:
  - #query: The passed-in $query.
  - #pre_render: $function with a _pre_render suffix.
  - #cache: An associative array prepared for drupal_render_cache_set().
```

## Code

```php
function drupal_render_cache_by_query($query, $function, $expire = CACHE_TEMPORARY, $granularity = NULL) {
  $cache_keys = array_merge(array($function), drupal_render_cid_parts($granularity));
  $query->preExecute();
  $cache_keys[] = hash('sha256', serialize(array((string) $query, $query->getArguments())));
  return array(
    '#query' => $query,
    '#pre_render' => array($function . '_pre_render'),
    '#cache' => array(
      'keys' => $cache_keys,
      'expire' => $expire,
    ),
  );
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
