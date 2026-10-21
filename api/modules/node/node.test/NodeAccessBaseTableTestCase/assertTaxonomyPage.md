# NodeAccessBaseTableTestCase::assertTaxonomyPage()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1286–1314 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1286-L1314)
- **Class:** [NodeAccessBaseTableTestCase](../NodeAccessBaseTableTestCase.md)
- **Module/theme:** node

## Signature

```php
protected function assertTaxonomyPage($is_admin)
```

## Documentation

```text
Checks taxonomy/term listings to ensure only accessible nodes are listed.

@param $is_admin
  A boolean indicating whether the current user is an administrator. If
  TRUE, all nodes should be listed. If FALSE, only public nodes and the
  user's own private nodes should be listed.
```

## Code

```php
  protected function assertTaxonomyPage($is_admin) {
    foreach (array($this->publicTid, $this->privateTid) as $tid_is_private => $tid) {
      $this->drupalGet("taxonomy/term/$tid");
      $this->nids_visible = array();
      foreach ($this->xpath("//a[text()='Read more']") as $link) {
        $this->assertTrue(preg_match('|node/(\d+)$|', (string) $link['href'], $matches), 'Read more points to a node');
        $this->nids_visible[$matches[1]] = TRUE;
      }
      foreach ($this->nodesByUser as $uid => $data) {
        foreach ($data as $nid => $is_private) {
          // Private nodes should be visible on the private term page,
          // public nodes should be visible on the public term page.
          $should_be_visible = $tid_is_private == $is_private;
          // Non-administrators can only see their own nodes on the private
          // term page.
          if (!$is_admin && $tid_is_private) {
            $should_be_visible = $should_be_visible && $uid == $this->webUser->uid;
          }
          $this->assertIdentical(isset($this->nids_visible[$nid]), $should_be_visible, strtr('A %private node by user %uid is %visible for user %current_uid on the %tid_is_private page.', array(
            '%private' => $is_private ? 'private' : 'public',
            '%uid' => $uid,
            '%visible' => isset($this->nids_visible[$nid]) ? 'visible' : 'not visible',
            '%current_uid' => $this->webUser->uid,
            '%tid_is_private' => $tid_is_private ? 'private' : 'public',
          )));
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
