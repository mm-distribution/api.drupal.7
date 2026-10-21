# ForumTestCase

- **Type:** Class
- **File:** [`modules/forum/forum.test`](_file.md), lines 11–669 · [local source](../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L11-L669)
- **Module/theme:** forum

## Signature

```php
class ForumTestCase extends DrupalWebTestCase
```

## Documentation

```text
Provides automated tests for the Forum module.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

```text
A user with various administrative privileges.
```

### $edit_own_topics_user

```php
protected $edit_own_topics_user;
```

```text
A user that can create forum topics and edit its own topics.
```

### $edit_any_topics_user

```php
protected $edit_any_topics_user;
```

```text
A user that can create, edit, and delete forum topics.
```

### $web_user

```php
protected $web_user;
```

```text
A user with no special privileges.
```

### $container

```php
protected $container;
```

```text
An array representing a container.
```

### $forum

```php
protected $forum;
```

```text
An array representing a forum.
```

### $root_forum

```php
protected $root_forum;
```

```text
An array representing a root forum.
```

### $nids

```php
protected $nids;
```

```text
An array of forum topic node IDs.
```

### $delete_forum

```php
protected $delete_forum;
```

```text
A forum to delete.
```

## Methods (derived index)

- [getInfo()](ForumTestCase/getInfo.md)
- [setUp()](ForumTestCase/setUp.md)
- [testEnableForumField()](ForumTestCase/testEnableForumField.md) — Tests disabling and re-enabling the Forum module.
- [testForum()](ForumTestCase/testForum.md) — Tests forum functionality through the admin and user interfaces.
- [testAddOrphanTopic()](ForumTestCase/testAddOrphanTopic.md) — Tests that forum nodes can't be added without a parent.
- [doAdminTests()](ForumTestCase/doAdminTests.md) — Runs admin tests on the admin user.
- [editForumTaxonomy()](ForumTestCase/editForumTaxonomy.md) — Edits the forum taxonomy.
- [createForum()](ForumTestCase/createForum.md) — Creates a forum container or a forum.
- [deleteForum()](ForumTestCase/deleteForum.md) — Deletes a forum.
- [doBasicTests()](ForumTestCase/doBasicTests.md) — Runs basic tests on the indicated user.
- [createForumTopic()](ForumTestCase/createForumTopic.md) — Creates forum topic.
- [verifyForums()](ForumTestCase/verifyForums.md) — Verifies that the logged in user has access to a forum nodes.
- [verifyForumView()](ForumTestCase/verifyForumView.md) — Verifies display of forum page.
- [generateForumTopics()](ForumTestCase/generateForumTopics.md) — Generates forum topics to test the display of an active forum block.
- [viewForumTopics()](ForumTestCase/viewForumTopics.md) — Views forum topics to test the display of an active forum block.

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
