# UrlAlterFunctionalTest::testUrlAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 148–192 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L148-L192)
- **Class:** [UrlAlterFunctionalTest](../UrlAlterFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testUrlAlter()
```

## Documentation

```text
Test that URL altering works and that it occurs in the correct order.
```

## Code

```php
  function testUrlAlter() {
    $account = $this->drupalCreateUser(array('administer url aliases'));
    $this->drupalLogin($account);

    $uid = $account->uid;
    $name = $account->name;

    // Test a single altered path.
    $this->assertUrlInboundAlter("user/$name", "user/$uid");
    $this->assertUrlOutboundAlter("user/$uid", "user/$name");

    // Test that a path always uses its alias.
    $path = array('source' => "user/$uid/test1", 'alias' => 'alias/test1');
    path_save($path);
    $this->assertUrlInboundAlter('alias/test1', "user/$uid/test1");
    $this->assertUrlOutboundAlter("user/$uid/test1", 'alias/test1');

    // Test that alias source paths are normalized in the interface.
    $edit = array('source' => "user/$name/edit", 'alias' => 'alias/test2');
    $this->drupalPost('admin/config/search/path/add', $edit, t('Save'));
    $this->assertText(t('The alias has been saved.'));

    // Test that a path always uses its alias.
    $this->assertUrlInboundAlter('alias/test2', "user/$uid/edit");
    $this->assertUrlOutboundAlter("user/$uid/edit", 'alias/test2');

    // Test a non-existent user is not altered.
    $uid++;
    $this->assertUrlInboundAlter("user/$uid", "user/$uid");
    $this->assertUrlOutboundAlter("user/$uid", "user/$uid");

    // Test that 'forum' is altered to 'community' correctly, both at the root
    // level and for a specific existing forum.
    $this->assertUrlInboundAlter('community', 'forum');
    $this->assertUrlOutboundAlter('forum', 'community');
    $forum_vid = db_query("SELECT vid FROM {taxonomy_vocabulary} WHERE module = 'forum'")->fetchField();
    $tid = db_insert('taxonomy_term_data')
      ->fields(array(
        'name' => $this->randomName(),
        'vid' => $forum_vid,
      ))
      ->execute();
    $this->assertUrlInboundAlter("community/$tid", "forum/$tid");
    $this->assertUrlOutboundAlter("forum/$tid", "community/$tid");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
