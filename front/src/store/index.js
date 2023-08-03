import React, { createContext, useContext } from "react";

import { currentUserStore } from "./auth/currentUserStore";



export const rootStore = {
  currentUserStore};

export const RootStoreContext = createContext({ rootStore });

export const useRootStore = () => useContext(RootStoreContext);

export const RootStoreProvider = ({ store, children }) => {
  return (
    <RootStoreContext.Provider value={store}>
      {children}
    </RootStoreContext.Provider>
  );
};
