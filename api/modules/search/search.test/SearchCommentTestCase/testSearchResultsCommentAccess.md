# SearchCommentTestCase::testSearchResultsCommentAccess()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 858–912 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L858-L912)
- **Class:** [SearchCommentTestCase](../SearchCommentTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchResultsCommentAccess()
```

## Documentation

```text
Verify access rules for comment indexing with different permissions.
```

## Code

```php
  function testSearchResultsCommentAccess() {
    $comment_body = 'Test comment body';
    $this->comment_subject = 'Test comment subject';
    $this->admin_role = $this->admin_user->roles;
    unset($this->admin_role[DRUPAL_AUTHENTICATED_RID]);
    $this->admin_role = key($this->admin_role);

    // Create a node.
    variable_set('comment_preview_article', DRUPAL_OPTIONAL);
    $this->node = $this->drupalCreateNode(array('type' => 'article'));

    // Post a comment using 'Full HTML' text format.
    $edit_comment = array();
    $edit_comment['subject'] = $this->comment_subject;
    $edit_comment['comment_body[' . LANGUAGE_NONE . '][0][value]'] = '<h1>' . $comment_body . '</h1>';
    $this->drupalPost('comment/reply/' . $this->node->nid, $edit_comment, t('Save'));

    $this->drupalLogout();
    $this->setRolePermissions(DRUPAL_ANONYMOUS_RID);
    $this->checkCommentAccess('Anon user has search permission but no access comments permission, comments should not be indexed');

    $this->setRolePermissions(DRUPAL_ANONYMOUS_RID, TRUE);
    $this->checkCommentAccess('Anon user has search permission and access comments permission, comments should be indexed', TRUE);

    $this->drupalLogin($this->admin_user);
    $this->drupalGet('admin/people/permissions');

    // Disable search access for authenticated user to test admin user.
    $this->setRolePermissions(DRUPAL_AUTHENTICATED_RID, FALSE, FALSE);

    $this->setRolePermissions($this->admin_role);
    $this->checkCommentAccess('Admin user has search permission but no access comments permission, comments should not be indexed');

    $this->setRolePermissions($this->admin_role, TRUE);
    $this->checkCommentAccess('Admin user has search permission and access comments permission, comments should be indexed', TRUE);

    $this->setRolePermissions(DRUPAL_AUTHENTICATED_RID);
    $this->checkCommentAccess('Authenticated user has search permission but no access comments permission, comments should not be indexed');

    $this->setRolePermissions(DRUPAL_AUTHENTICATED_RID, TRUE);
    $this->checkCommentAccess('Authenticated user has search permission and access comments permission, comments should be indexed', TRUE);

    // Verify that access comments permission is inherited from the
    // authenticated role.
    $this->setRolePermissions(DRUPAL_AUTHENTICATED_RID, TRUE, FALSE);
    $this->setRolePermissions($this->admin_role);
    $this->checkCommentAccess('Admin user has search permission and no access comments permission, but comments should be indexed because admin user inherits authenticated user\'s permission to access comments', TRUE);

    // Verify that search content permission is inherited from the authenticated
    // role.
    $this->setRolePermissions(DRUPAL_AUTHENTICATED_RID, TRUE, TRUE);
    $this->setRolePermissions($this->admin_role, TRUE, FALSE);
    $this->checkCommentAccess('Admin user has access comments permission and no search permission, but comments should be indexed because admin user inherits authenticated user\'s permission to search', TRUE);

  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
