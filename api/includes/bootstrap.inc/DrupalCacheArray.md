# DrupalCacheArray

- **Type:** Class
- **File:** [`includes/bootstrap.inc`](_file.md), lines 320–470 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L320-L470)

## Signature

```php
abstract class DrupalCacheArray implements ArrayAccess
```

## Documentation

```text
Provides a caching wrapper to be used in place of large array structures.

This class should be extended by systems that need to cache large amounts
of data and have it represented as an array to calling functions. These
arrays can become very large, so ArrayAccess is used to allow different
strategies to be used for caching internally (lazy loading, building caches
over time etc.). This can dramatically reduce the amount of data that needs
to be loaded from cache backends on each request, and memory usage from
static caches of that same data.

Note that array_* functions do not work with ArrayAccess. Systems using
DrupalCacheArray should use this only internally. If providing API functions
that return the full array, this can be cached separately or returned
directly. However since DrupalCacheArray holds partial content by design, it
should be a normal PHP array or otherwise contain the full structure.

Note also that due to limitations in PHP prior to 5.3.4, it is impossible to
write directly to the contents of nested arrays contained in this object.
Only writes to the top-level array elements are possible. So if you
previously had set $object['foo'] = array(1, 2, 'bar' => 'baz'), but later
want to change the value of 'bar' from 'baz' to 'foobar', you cannot do so
a targeted write like $object['foo']['bar'] = 'foobar'. Instead, you must
overwrite the entire top-level 'foo' array with the entire set of new
values: $object['foo'] = array(1, 2, 'bar' => 'foobar'). Due to this same
limitation, attempts to create references to any contained data, nested or
otherwise, will fail silently. So $var = &$object['foo'] will not throw an
error, and $var will be populated with the contents of $object['foo'], but
that data will be passed by value, not reference. For more information on
the PHP limitation, see the note in the official PHP documentation at·
http://php.net/manual/arrayaccess.offsetget.php on
ArrayAccess::offsetGet().

By default, the class accounts for caches where calling functions might
request keys in the array that won't exist even after a cache rebuild. This
prevents situations where a cache rebuild would be triggered over and over
due to a 'missing' item. These cases are stored internally as a value of
NULL. This means that the offsetGet() and offsetExists() methods
must be overridden if caching an array where the top level values can
legitimately be NULL, and where $object->offsetExists() needs to correctly
return (equivalent to array_key_exists() vs. isset()). This should not
be necessary in the majority of cases.

Classes extending this class must override at least the
resolveCacheMiss() method to have a working implementation.

offsetSet() is not overridden by this class by default. In practice this
means that assigning an offset via arrayAccess will only apply while the
object is in scope and will not be written back to the persistent cache.
This follows a similar pattern to static vs. persistent caching in
procedural code. Extending classes may wish to alter this behavior, for
example by overriding offsetSet() and adding an automatic call to persist().

@see SchemaCache
```

## Properties

### $cid

```php
protected $cid;
```

```text
A cid to pass to cache_set() and cache_get().
```

### $bin

```php
protected $bin;
```

```text
A bin to pass to cache_set() and cache_get().
```

### $keysToPersist

```php
protected $keysToPersist = array();
```

```text
An array of keys to add to the cache at the end of the request.
```

### $storage

```php
protected $storage = array();
```

```text
Storage for the data itself.
```

## Methods (derived index)

- [__construct()](DrupalCacheArray/__construct.md) — Constructs a DrupalCacheArray object.
- [offsetExists()](DrupalCacheArray/offsetExists.md)
- [offsetGet()](DrupalCacheArray/offsetGet.md)
- [offsetSet()](DrupalCacheArray/offsetSet.md)
- [offsetUnset()](DrupalCacheArray/offsetUnset.md)
- [persist()](DrupalCacheArray/persist.md) — Flags an offset value to be written to the persistent cache.
- [resolveCacheMiss()](DrupalCacheArray/resolveCacheMiss.md) — Resolves a cache miss.
- [set()](DrupalCacheArray/set.md) — Writes a value to the persistent cache immediately.
- [__destruct()](DrupalCacheArray/__destruct.md) — Destructs the DrupalCacheArray object.

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
