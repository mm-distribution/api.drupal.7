# NodeAdminTestCase::testContentAdminPages()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1868–1959 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1868-L1959)
- **Class:** [NodeAdminTestCase](../NodeAdminTestCase.md)
- **Module/theme:** node

## Signature

```php
function testContentAdminPages()
```

## Documentation

```text
Tests content overview with different user permissions.

Taxonomy filters are tested separately.

@see TaxonomyNodeFilterTestCase
```

## Code

```php
  function testContentAdminPages() {
    $this->drupalLogin($this->admin_user);

    $nodes['published_page'] = $this->drupalCreateNode(array('type' => 'page'));
    $nodes['published_article'] = $this->drupalCreateNode(array('type' => 'article'));
    $nodes['unpublished_page_1'] = $this->drupalCreateNode(array('type' => 'page', 'uid' => $this->base_user_1->uid, 'status' => 0));
    $nodes['unpublished_page_2'] = $this->drupalCreateNode(array('type' => 'page', 'uid' => $this->base_user_2->uid, 'status' => 0));

    // Verify view, edit, and delete links for any content.
    $this->drupalGet('admin/content');
    $this->assertResponse(200);
    foreach ($nodes as $node) {
      $this->assertLinkByHref('node/' . $node->nid);
      $this->assertLinkByHref('node/' . $node->nid . '/edit');
      $this->assertLinkByHref('node/' . $node->nid . '/delete');
      // Verify tableselect.
      $this->assertFieldByName('nodes[' . $node->nid . ']', '', 'Tableselect found.');
    }

    // Verify filtering by publishing status.
    $edit = array(
      'status' => 'status-1',
    );
    $this->drupalPost(NULL, $edit, t('Filter'));

    $this->assertRaw(t('where %property is %value', array('%property' => t('status'), '%value' => 'published')), 'Content list is filtered by status.');

    $this->assertLinkByHref('node/' . $nodes['published_page']->nid . '/edit');
    $this->assertLinkByHref('node/' . $nodes['published_article']->nid . '/edit');
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_1']->nid . '/edit');

    // Verify filtering by status and content type.
    $edit = array(
      'type' => 'page',
    );
    $this->drupalPost(NULL, $edit, t('Refine'));

    $this->assertRaw(t('where %property is %value', array('%property' => t('status'), '%value' => 'published')), 'Content list is filtered by status.');
    $this->assertRaw(t('and where %property is %value', array('%property' => t('type'), '%value' => 'Basic page')), 'Content list is filtered by content type.');

    $this->assertLinkByHref('node/' . $nodes['published_page']->nid . '/edit');
    $this->assertNoLinkByHref('node/' . $nodes['published_article']->nid . '/edit');

    // Verify no operation links are displayed for regular users.
    $this->drupalLogout();
    $this->drupalLogin($this->base_user_1);
    $this->drupalGet('admin/content');
    $this->assertResponse(200);
    $this->assertLinkByHref('node/' . $nodes['published_page']->nid);
    $this->assertLinkByHref('node/' . $nodes['published_article']->nid);
    $this->assertNoLinkByHref('node/' . $nodes['published_page']->nid . '/edit');
    $this->assertNoLinkByHref('node/' . $nodes['published_page']->nid . '/delete');
    $this->assertNoLinkByHref('node/' . $nodes['published_article']->nid . '/edit');
    $this->assertNoLinkByHref('node/' . $nodes['published_article']->nid . '/delete');

    // Verify no unpublished content is displayed without permission.
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_1']->nid);
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_1']->nid . '/edit');
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_1']->nid . '/delete');

    // Verify no tableselect.
    $this->assertNoFieldByName('nodes[' . $nodes['published_page']->nid . ']', '', 'No tableselect found.');

    // Verify unpublished content is displayed with permission.
    $this->drupalLogout();
    $this->drupalLogin($this->base_user_2);
    $this->drupalGet('admin/content');
    $this->assertResponse(200);
    $this->assertLinkByHref('node/' . $nodes['unpublished_page_2']->nid);
    // Verify no operation links are displayed.
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_2']->nid . '/edit');
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_2']->nid . '/delete');

    // Verify user cannot see unpublished content of other users.
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_1']->nid);
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_1']->nid . '/edit');
    $this->assertNoLinkByHref('node/' . $nodes['unpublished_page_1']->nid . '/delete');

    // Verify no tableselect.
    $this->assertNoFieldByName('nodes[' . $nodes['unpublished_page_2']->nid . ']', '', 'No tableselect found.');

    // Verify node access can be bypassed.
    $this->drupalLogout();
    $this->drupalLogin($this->base_user_3);
    $this->drupalGet('admin/content');
    $this->assertResponse(200);
    foreach ($nodes as $node) {
      $this->assertLinkByHref('node/' . $node->nid);
      $this->assertLinkByHref('node/' . $node->nid . '/edit');
      $this->assertLinkByHref('node/' . $node->nid . '/delete');
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
