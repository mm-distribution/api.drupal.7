# TrackerTest

- **Type:** Class
- **File:** [`modules/tracker/tracker.test`](_file.md), lines 11–333 · [local source](../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L11-L333)
- **Module/theme:** tracker

## Signature

```php
class TrackerTest extends DrupalWebTestCase
```

## Documentation

```text
Defines a base class for testing tracker.module.
```

## Properties

### $user

```php
protected $user;
```

```text
The main user for testing.

@var object
```

### $other_user

```php
protected $other_user;
```

```text
A second user that will 'create' comments and nodes.

@var object
```

## Methods (derived index)

- [getInfo()](TrackerTest/getInfo.md)
- [setUp()](TrackerTest/setUp.md)
- [testTrackerAll()](TrackerTest/testTrackerAll.md) — Tests for the presence of nodes on the global tracker listing.
- [testTrackerUser()](TrackerTest/testTrackerUser.md) — Tests for the presence of nodes on a user's tracker listing.
- [testTrackerNewNodes()](TrackerTest/testTrackerNewNodes.md) — Tests for the presence of the "new" flag for nodes.
- [testTrackerNewComments()](TrackerTest/testTrackerNewComments.md) — Tests for comment counters on the tracker listing.
- [testTrackerOrderingNewComments()](TrackerTest/testTrackerOrderingNewComments.md) — Tests for ordering on a users tracker listing when comments are posted.
- [testTrackerCronIndexing()](TrackerTest/testTrackerCronIndexing.md) — Tests that existing nodes are indexed by cron.
- [testTrackerAdminUnpublish()](TrackerTest/testTrackerAdminUnpublish.md) — Tests that publish/unpublish works at admin/content/node.

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
