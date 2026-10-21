# Update Manager module: file management

- **Topic id:** `update_manager_file`
- **Defined in:** [`modules/update/update.manager.inc`](../modules/update/update.manager.inc/_file.md), line 753 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L753)

## Documentation

```text
@defgroup update_manager_file Update Manager module: file management
@{
Update Manager module file management functions.

These functions are used by the update manager to copy, extract, and verify
archive files.
```

## Members (derived, 6)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [hook_verify_update_archive()](../modules/update/update.api.php/hook_verify_update_archive.md) (function) — Verify an archive after it has been downloaded and extracted.
- [update_manager_archive_extract()](../modules/update/update.manager.inc/update_manager_archive_extract.md) (function) — Unpacks a downloaded archive file.
- [update_manager_archive_verify()](../modules/update/update.manager.inc/update_manager_archive_verify.md) (function) — Verifies an archive after it has been downloaded and extracted.
- [update_manager_batch_project_get()](../modules/update/update.manager.inc/update_manager_batch_project_get.md) (function) — Implements callback_batch_operation().
- [update_manager_file_get()](../modules/update/update.manager.inc/update_manager_file_get.md) (function) — Copies a file from the specified URL to the temporary directory for updates.
- [update_manager_local_transfers_allowed()](../modules/update/update.manager.inc/update_manager_local_transfers_allowed.md) (function) — Determines if file transfers will be performed locally.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
