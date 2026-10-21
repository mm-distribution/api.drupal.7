# SearchCommentCountToggleTestCase

- **Type:** Class
- **File:** [`modules/search/search.test`](_file.md), lines 1053–1133 · [local source](../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1053-L1133)
- **Module/theme:** search

## Signature

```php
class SearchCommentCountToggleTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests that comment count display toggles properly on comment status of node

Issue 537278

- Nodes with comment status set to Open should always how comment counts
- Nodes with comment status set to Closed should show comment counts
    only when there are comments
- Nodes with comment status set to Hidden should never show comment counts
```

## Properties

### $searching_user

```php
protected $searching_user;
```

### $searchable_nodes

```php
protected $searchable_nodes;
```

## Methods (derived index)

- [getInfo()](SearchCommentCountToggleTestCase/getInfo.md)
- [setUp()](SearchCommentCountToggleTestCase/setUp.md)
- [testSearchCommentCountToggle()](SearchCommentCountToggleTestCase/testSearchCommentCountToggle.md) — Verify that comment count display toggles properly on comment status of node

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
