# modules/update/update.manager.inc

- **Source:** [local](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · 948 lines
- **Module/theme:** update

## File documentation

```text
@file
Administrative screens and processing functions of the Update Manager module.

This allows site administrators with the 'administer software updates'
permission to either upgrade existing projects, or download and install new
ones, so long as the killswitch setting ('allow_authorize_operations') is
still TRUE.

To install new code, the administrator is prompted for either the URL of an
archive file, or to directly upload the archive file. The archive is loaded
into a temporary location, extracted, and verified. If everything is
successful, the user is redirected to authorize.php to type in file transfer
credentials and authorize the installation to proceed with elevated
privileges, such that the extracted files can be copied out of the temporary
location and into the live web root.

Updating existing code is a more elaborate process. The first step is a
selection form where the user is presented with a table of installed projects
that are missing newer releases. The user selects which projects they wish to
update, and presses the "Download updates" button to continue. This sets up a
batch to fetch all the selected releases, and redirects to
admin/update/download to display the batch progress bar as it runs. Each
batch operation is responsible for downloading a single file, extracting the
archive, and verifying the contents. If there are any errors, the user is
redirected back to the first page with the error messages. If all downloads
were extacted and verified, the user is instead redirected to
admin/update/ready, a landing page which reminds them to backup their
database and asks if they want to put the site offline during the update.
Once the user presses the "Install updates" button, they are redirected to
authorize.php to supply their web root file access credentials. The
authorized operation (which lives in update.authorize.inc) sets up a batch to
copy each extracted update from the temporary location into the live web
root.
```

## Functions (derived index)

- [update_manager_update_form()](update_manager_update_form.md) — Form constructor for the update form of the Update Manager module.
- [theme_update_manager_update_form()](theme_update_manager_update_form.md) — Returns HTML for the first page in the process of updating projects.
- [update_manager_update_form_validate()](update_manager_update_form_validate.md) — Form validation handler for update_manager_update_form().
- [update_manager_update_form_submit()](update_manager_update_form_submit.md) — Form submission handler for update_manager_update_form().
- [update_manager_download_batch_finished()](update_manager_download_batch_finished.md) — Implements callback_batch_finished().
- [update_manager_update_ready_form()](update_manager_update_ready_form.md) — Form constructor for the update ready form.
- [update_manager_update_ready_form_submit()](update_manager_update_ready_form_submit.md) — Form submission handler for update_manager_update_ready_form().
- [update_manager_install_form()](update_manager_install_form.md) — Form constructor for the install form of the Update Manager module.
- [_update_manager_check_backends()](_update_manager_check_backends.md) — Checks for file transfer backends and prepares a form fragment about them.
- [update_manager_install_form_validate()](update_manager_install_form_validate.md) — Form validation handler for update_manager_install_form().
- [update_manager_install_form_submit()](update_manager_install_form_submit.md) — Form submission handler for update_manager_install_form().
- [update_manager_archive_extract()](update_manager_archive_extract.md) — Unpacks a downloaded archive file.
- [update_manager_archive_verify()](update_manager_archive_verify.md) — Verifies an archive after it has been downloaded and extracted.
- [update_manager_file_get()](update_manager_file_get.md) — Copies a file from the specified URL to the temporary directory for updates.
- [update_manager_batch_project_get()](update_manager_batch_project_get.md) — Implements callback_batch_operation().
- [update_manager_local_transfers_allowed()](update_manager_local_transfers_allowed.md) — Determines if file transfers will be performed locally.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
