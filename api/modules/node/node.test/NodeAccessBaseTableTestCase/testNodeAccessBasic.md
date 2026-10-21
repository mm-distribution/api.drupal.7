# NodeAccessBaseTableTestCase::testNodeAccessBasic()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1194–1276 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1194-L1276)
- **Class:** [NodeAccessBaseTableTestCase](../NodeAccessBaseTableTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeAccessBasic()
```

## Documentation

```text
Tests the "private" node access functionality.

- Create 2 users with "access content" and "create article" permissions.
- Each user creates one private and one not private article.

- Test that each user can view the other user's non-private article.
- Test that each user cannot view the other user's private article.
- Test that each user finds only appropriate (non-private + own private)
  in taxonomy listing.
- Create another user with 'view any private content'.
- Test that user 4 can view all content created above.
- Test that user 4 can view all content on taxonomy listing.
```

## Code

```php
  function testNodeAccessBasic() {
    $num_simple_users = 2;
    $simple_users = array();

    // nodes keyed by uid and nid: $nodes[$uid][$nid] = $is_private;
    $this->nodesByUser = array();
    $titles = array(); // Titles keyed by nid
    $private_nodes = array(); // Array of nids marked private.
    for ($i = 0; $i < $num_simple_users; $i++) {
      $simple_users[$i] = $this->drupalCreateUser(array('access content', 'create article content'));
    }
    foreach ($simple_users as $this->webUser) {
      $this->drupalLogin($this->webUser);
      foreach (array(0 => 'Public', 1 => 'Private') as $is_private => $type) {
        $edit = array(
          'title' => t('@private_public Article created by @user', array('@private_public' => $type, '@user' => $this->webUser->name)),
        );
        if ($is_private) {
          $edit['private'] = TRUE;
          $edit['body[und][0][value]'] = 'private node';
          $edit['field_tags[und]'] = 'private';
        }
        else {
          $edit['body[und][0][value]'] = 'public node';
          $edit['field_tags[und]'] = 'public';
        }

        $this->drupalPost('node/add/article', $edit, t('Save'));
        $nid = db_query('SELECT nid FROM {node} WHERE title = :title', array(':title' => $edit['title']))->fetchField();
        $private_status = db_query('SELECT private FROM {node_access_test} where nid = :nid', array(':nid' => $nid))->fetchField();
        $this->assertTrue($is_private == $private_status, 'The private status of the node was properly set in the node_access_test table.');
        if ($is_private) {
          $private_nodes[] = $nid;
        }
        $titles[$nid] = $edit['title'];
        $this->nodesByUser[$this->webUser->uid][$nid] = $is_private;
      }
    }
    $this->publicTid = db_query('SELECT tid FROM {taxonomy_term_data} WHERE name = :name', array(':name' => 'public'))->fetchField();
    $this->privateTid = db_query('SELECT tid FROM {taxonomy_term_data} WHERE name = :name', array(':name' => 'private'))->fetchField();
    $this->assertTrue($this->publicTid, 'Public tid was found');
    $this->assertTrue($this->privateTid, 'Private tid was found');
    foreach ($simple_users as $this->webUser) {
      $this->drupalLogin($this->webUser);
      // Check own nodes to see that all are readable.
      foreach ($this->nodesByUser as $uid => $data) {
        foreach ($data as $nid => $is_private) {
          $this->drupalGet('node/' . $nid);
          if ($is_private) {
            $should_be_visible = $uid == $this->webUser->uid;
          }
          else {
            $should_be_visible = TRUE;
          }
          $this->assertResponse($should_be_visible ? 200 : 403, strtr('A %private node by user %uid is %visible for user %current_uid.', array(
            '%private' => $is_private ? 'private' : 'public',
            '%uid' => $uid,
            '%visible' => $should_be_visible ? 'visible' : 'not visible',
            '%current_uid' => $this->webUser->uid,
          )));
        }
      }

      // Check to see that the correct nodes are shown on taxonomy/private
      // and taxonomy/public.
      $this->assertTaxonomyPage(FALSE);
    }

    // Now test that a user with 'access any private content' can view content.
    $access_user = $this->drupalCreateUser(array('access content', 'create article content', 'node test view', 'search content'));
    $this->drupalLogin($access_user);

    foreach ($this->nodesByUser as $uid => $private_status) {
      foreach ($private_status as $nid => $is_private) {
        $this->drupalGet('node/' . $nid);
        $this->assertResponse(200);
      }
    }

    // This user should be able to see all of the nodes on the relevant
    // taxonomy pages.
    $this->assertTaxonomyPage(TRUE);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
