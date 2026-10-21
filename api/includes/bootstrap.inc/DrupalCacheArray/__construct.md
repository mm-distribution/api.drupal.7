# DrupalCacheArray::__construct()

- **Type:** Method
- **File:** [`includes/bootstrap.inc`](../_file.md), lines 350–357 · [local source](../../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L350-L357)
- **Class:** [DrupalCacheArray](../DrupalCacheArray.md)

## Signature

```php
public function __construct($cid, $bin)
```

## Documentation

```text
Constructs a DrupalCacheArray object.

@param $cid
  The cid for the array being cached.
@param $bin
  The bin to cache the array.
```

## Code

```php
  public function __construct($cid, $bin) {
    $this->cid = $cid;
    $this->bin = $bin;

    if ($cached = cache_get($this->cid, $this->bin)) {
     $this->storage = $cached->data;
    }
  }
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
