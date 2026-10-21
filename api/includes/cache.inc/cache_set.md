# cache_set()

- **Type:** Function
- **File:** [`includes/cache.inc`](_file.md), lines 141–143 · [local source](../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L141-L143)

## Signature

```php
function cache_set($cid, $data, $bin = 'cache', $expire = CACHE_PERMANENT)
```

## Documentation

```text
Stores data in the persistent cache.

The persistent cache is split up into several cache bins. In the default
cache implementation, each cache bin corresponds to a database table by the
same name. Other implementations might want to store several bins in data
structures that get flushed together. While it is not a problem for most
cache bins if the entries in them are flushed before their expire time, some
might break functionality or are extremely expensive to recalculate. The
other bins are expired automatically by core. Contributed modules can add
additional bins and get them expired automatically by implementing
hook_flush_caches().

The reasons for having several bins are as follows:
- Smaller bins mean smaller database tables and allow for faster selects and
  inserts.
- We try to put fast changing cache items and rather static ones into
  different bins. The effect is that only the fast changing bins will need a
  lot of writes to disk. The more static bins will also be better cacheable
  with MySQL's query cache.

@param $cid
  The cache ID of the data to store.
@param $data
  The data to store in the cache. Complex data types will be automatically
  serialized before insertion. Strings will be stored as plain text and are
  not serialized. Some storage engines only allow objects up to a maximum of
  1MB in size to be stored by default. When caching large arrays or similar,
  take care to ensure $data does not exceed this size.
@param $bin
  (optional) The cache bin to store the data in. Valid core values are:
  - cache: (default) Generic cache storage bin (used for theme registry,
    locale date, list of simpletest tests, etc.).
  - cache_block: Stores the content of various blocks.
  - cache_bootstrap: Stores the class registry, the system list of modules,
    the list of which modules implement which hooks, and the Drupal variable
    list.
  - cache_field: Stores the field data belonging to a given object.
  - cache_filter: Stores filtered pieces of content.
  - cache_form: Stores multistep forms. Flushing this bin means that some
    forms displayed to users lose their state and the data already submitted
    to them. This bin should not be flushed before its expired time.
  - cache_menu: Stores the structure of visible navigation menus per page.
  - cache_page: Stores generated pages for anonymous users. It is flushed
    very often, whenever a page changes, at least for every node and comment
    submission. This is the only bin affected by the page cache setting on
    the administrator panel.
  - cache_path: Stores the system paths that have an alias.
@param $expire
  (optional) Controls the maximum lifetime of this cache entry. Note that
  caches might be subject to clearing at any time, so this setting does not
  guarantee a minimum lifetime. With this in mind, the cache should not be
  used for data that must be kept during a cache clear, like sessions.

  Use one of the following values:
  - CACHE_PERMANENT: Indicates that the item should never be removed unless
    explicitly told to using cache_clear_all() with a cache ID.
  - CACHE_TEMPORARY: Indicates that the item should be removed at the next
    general cache wipe.
  - A Unix timestamp: Indicates that the item should be kept at least until
    the given time, after which it behaves like CACHE_TEMPORARY.

@see _update_cache_set()
@see cache_get()
```

## Code

```php
function cache_set($cid, $data, $bin = 'cache', $expire = CACHE_PERMANENT) {
  return _cache_get_object($bin)->set($cid, $data, $expire);
}
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
