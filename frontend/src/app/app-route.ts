import { Routes } from '@angular/router';

export const rootRouterConfig: Routes = [
  {path: '', loadChildren: () => import('./pages/pages.routes').then(m => m.PagesRoute)},
];
